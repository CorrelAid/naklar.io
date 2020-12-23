import { trigger, transition, style, stagger, animate, query } from '@angular/animations';
import { Component, HostBinding, OnInit } from '@angular/core';
import { add, compareAsc, isAfter } from 'date-fns';
import { BehaviorSubject, combineLatest, interval, Observable } from 'rxjs';
import { filter, map, startWith, switchMap } from 'rxjs/operators';
import { Appointment } from 'src/app/_models/scheduling';
import { AppointmentService } from 'src/app/_services/database/scheduling/appointment.service';

@Component({
    selector: 'scheduling-appointment-list',
    templateUrl: './appointment-list.component.html',
    styleUrls: ['./appointment-list.component.scss'],
    animations: [
        trigger('appointmentTrigger', [
            transition('* => *', [
                query(':enter', [
                    style({ opacity: 0, transform: 'translateX(-100vw)'}),
                    stagger('100ms', animate('250ms ease', style({ opacity: 1, transform: 'none'}))),
                ]),
            ]),
        ])
    ]
})
export class AppointmentListComponent implements OnInit {
    refresh$ = new BehaviorSubject(null);
    autoRefresh$ = interval(1000 * 30).pipe(startWith(0));
    appointments$: Observable<Appointment[]>;

    constructor(private appointments: AppointmentService) {}

    ngOnInit(): void {
        this.appointments$ = combineLatest([this.refresh$, this.autoRefresh$]).pipe(
            switchMap(() =>
                this.appointments
                    .list()
                    .pipe(
                        map((appointments) =>
                            appointments
                                .sort((a, b) => compareAsc(a.startTime, b.startTime))
                                .filter((ap) => isAfter(add(ap.startTime, ap.duration), new Date()))
                        )
                    )
            )
        );
    }
    refresh() {
        this.refresh$.next(null);
    }

    trackAppointment(index: number, app: Appointment) {
      return app.id;
    }
}