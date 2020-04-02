import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { BehaviorSubject, Observable, throwError } from "rxjs";
import {
  User,
  SendableUser,
  SendableLogin,
  sendableToLocal
} from "../_models";
import { environment } from "../../environments/environment";

@Injectable({ providedIn: "root" })
export class AuthenticationService {
  private currentUserSubject: BehaviorSubject<User>;

  public currentUser: Observable<User>;

  constructor(private http: HttpClient) {
    this.currentUserSubject = new BehaviorSubject<User>(new User());
    this.currentUser = this.currentUserSubject.asObservable();
  }

  public get currentUserValue() {
    return this.currentUserSubject.value;
  }

  public register(user: SendableUser): void {
    this.http
      .post<SendableUser>(`${environment.apiUrl}/account/create/`, user)
      .subscribe(
        user => {
          console.log("HTTP Response: ", user);
          const u = sendableToLocal(user);
          console.log("converted: ", u);
          this.currentUserSubject.next(u);
        },
        error => {
          console.log(error);
          return throwError(error);
        }
      );
  }

  public login(login: SendableLogin): void {
    this.http
      .post<SendableLogin>(`${environment.apiUrl}/account/login/`, login)
      .subscribe(
        user => {
          console.log("HTTP Response: ", user);
        },
        error => {
          console.log(error);
          return throwError(error);
        }
      );
  }

  // TODO:
  public logout(): void {
    this.http.post(`${environment.apiUrl}/account/logout/`, null);
    this.currentUserSubject.next(null);
  }

  public logoutAll():void {
      this.http.post(`${environment.apiUrl}/account/logoutall/`, null)
  }
}