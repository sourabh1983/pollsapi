import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { Poll } from './poll';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PollService {

  private pollUrl = '/api/polls';

  constructor(private http: HttpClient) { }

  getPollList(): Observable<Poll[]> {
    const headers = new HttpHeaders().append('Authorization', 'Token d9099b2f85c53d6155c8a8294f34e2033037c3df')
    return this.http.get<Poll[]>(this.pollUrl, {headers});
  }
}
