import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { FormBuilder } from '@angular/forms'
import { Router } from '@angular/router'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private userService: UserService, private formBuilder: FormBuilder, private router: Router) { }

  form = this.formBuilder.group({
    username: '',
  });

  ngOnInit(): void {

  }

  onGo(){
    this.userService.newUser(this.form.value.username).subscribe( response => {
      // route to home
      console.log(response);
      this.router.navigate(['home']);
    },
    error => {
      console.log(error);
    });
  }

}
