import { Component, OnInit } from '@angular/core';
import { PollService } from '../poll.service';
import { Poll } from '../poll';

@Component({
  selector: 'app-poll-list',
  templateUrl: './poll-list.component.html',
  styleUrls: ['./poll-list.component.css']
})
export class PollListComponent implements OnInit {
  polls: Poll[];

  constructor(private pollService: PollService) { }

  ngOnInit() {
    this.getPollList();
  }

  private getPollList() : void {
    this.pollService.getPollList()
    .subscribe(polls => this.polls = polls);
  }
}
