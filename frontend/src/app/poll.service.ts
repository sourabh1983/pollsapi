import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { Poll } from './poll';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import { AppUser } from './app-user';
import {catchError} from "rxjs/operators";
import {throwError} from "rxjs/internal/observable/throwError";

@Injectable({
  providedIn: 'root'
})
export class PollService {

  private pollUrl = '/polls/';

  constructor(private http: HttpClient) { }

  getPollList(): Observable<Poll[]> {
    const headers = new HttpHeaders().append('Authorization', 'Token 0e1ceeb61b82a41d8d1a2c564983d756c398c24b');
    return this.http.get<Poll[]>(this.pollUrl, {headers});
  }

  /** POST: add a new hero to the database */
  addHero (user: AppUser): Observable<AppUser> {
    return this.http.post<AppUser>('/polls/login', user)
      .pipe(
      );
  }
}
