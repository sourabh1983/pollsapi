import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { Poll } from './poll';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PollService {

  private pollUrl = '/polls/';

  constructor(private http: HttpClient) { }

  getPollList(): Observable<Poll[]> {
    const headers = new HttpHeaders().append('Authorization', 'Token 0e1ceeb61b82a41d8d1a2c564983d756c398c24b')
    return this.http.get<Poll[]>(this.pollUrl, {headers});
  }
}
