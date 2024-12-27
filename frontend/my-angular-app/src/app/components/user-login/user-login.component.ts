// user-login.component.ts
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router'; 

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css'],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class UserLoginComponent {
  loginForm!: FormGroup;

  constructor(
    private fb: FormBuilder,
    private router: Router
  ) { 
    this.loginForm = this.fb.group({
      username: ['', [Validators.required, Validators.usernamevalidator]],
      password: ['', Validators.required]
    });
  }

  onSubmit() {
    if (this.loginForm.valid) {
      // Handle form submission logic here
      // Example: 
      const userData = this.loginForm.value; 
      console.log('User Data:', userData); 

      // Assuming you have a login service
      // this.authService.login(userData).subscribe(
      //   (response) => {
      //     // Handle successful login 
      //     // e.g., store token, redirect to dashboard
      //     // this.router.navigate(['/dashboard']); 
      //   },
      //   (error) => {
      //     // Handle login error
      //     console.error('Login Error:', error); 
      //     // Display error message to the user
      //   }
      // );
    }
  }
}