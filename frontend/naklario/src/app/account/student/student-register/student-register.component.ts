import { Component, OnInit } from "@angular/core";

import {
  State,
  SchoolType,
  SchoolData,
  states,
  schoolData,
  schoolTypes,
  SendableUser,
} from "../../../_models/database";
import { first } from "rxjs/operators";
import { Options } from "ng5-slider";
import { AuthenticationService } from "../../../_services";
import { FormBuilder, Validators } from "@angular/forms";
import { passwordNotMatchValidator } from "../../../_helpers";
import { Router, ActivatedRoute } from "@angular/router";

@Component({
  selector: "app-student-register",
  templateUrl: "./student-register.component.html",
  styleUrls: ["./student-register.component.scss"],
})
export class StudentRegisterComponent implements OnInit {
  states: State[] = states;
  schoolTypes: SchoolType[] = schoolTypes;
  schoolData: SchoolData[] = schoolData;

  registerForm = this.fb.group(
    {
      firstName: ["", Validators.required],
      lastName: ["", Validators.required],
      email: ["", [Validators.required, Validators.email]],
      password: ["", [Validators.required, Validators.minLength(8)]],
      passwordRepeat: ["", [Validators.required, Validators.minLength(8)]],
      state: [null, Validators.required],
      schoolType: [null, Validators.required],
      slider: [10, Validators.required],
      terms: [false, Validators.requiredTrue],
    },
    { validators: passwordNotMatchValidator }
  );

  // slider controls
  options: Options = {
    animate: false,
    showTicks: true,
    floor: 5,
    ceil: 13,
  };

  submitted = false;
  submitSuccess = false;
  loading = false;
  error: string = null;

  get f() {
    return this.registerForm.controls;
  }

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private route: ActivatedRoute,
    private authenticationService: AuthenticationService
  ) {}

  ngOnInit(): void {}

  onSubmit(): void {
    this.submitted = true;

    if (this.registerForm.invalid) {
      return;
    }

    const user: SendableUser = {
      email: this.f.email.value,
      password: this.f.password.value,
      first_name: this.f.firstName.value,
      last_name: this.f.lastName.value,
      state: this.f.state.value.id,
      terms_accepted: this.f.terms.value,
      studentdata: {
        school_data: this.schoolData.find(
          (x) =>
            x.grade === this.f.slider.value &&
            x.school_type === this.f.schoolType.value.id
        ).id,
      },
      tutordata: null,
    };
    console.log("About to send student Data: ", user);

    this.loading = true;
    this.authenticationService
      .register(user)
      .pipe(first())
      .subscribe(
        (data) => {
          this.loading = false;
          this.submitSuccess = true;
          this.error = null;
          this.router.navigate(["/roulette/student"]);
        },
        (error) => {
          this.error = error;
          this.loading = false;
        }
      );
  }
}
