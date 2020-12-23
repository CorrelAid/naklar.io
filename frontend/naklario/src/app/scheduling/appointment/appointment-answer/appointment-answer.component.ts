import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { Observable, of, throwError } from 'rxjs';
import { catchError, switchMap } from 'rxjs/operators';
import { Appointment } from 'src/app/_models/scheduling';
import { AppointmentService } from 'src/app/_services/database/scheduling/appointment.service';

@Component({
    selector: 'scheduling-appointment-answer',
    templateUrl: './appointment-answer.component.html',
    styleUrls: ['./appointment-answer.component.scss'],
})
export class AppointmentAnswerComponent implements OnInit {
    appointment$: Observable<Appointment>;
    error: any = null;

    constructor(private appointments: AppointmentService, private route: ActivatedRoute) {}

    ngOnInit(): void {
        this.appointment$ = this.route.params.pipe(
            switchMap((params: {id: string}) => {
                return this.appointments.read(parseInt(params.id, 10));
            }),
            catchError((err) => {
              this.error = err;
              console.log(err);
              return throwError(err);
            })
        );
    }
}