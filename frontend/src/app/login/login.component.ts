import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  appUser: FormGroup;
  constructor() { }

  ngOnInit() {
    this.appUser = new FormGroup({
      'username': new FormControl(),
      'password': new FormControl()
    });
  }

  validateUser() {
    console.log(this.appUser.value);
  }

}
