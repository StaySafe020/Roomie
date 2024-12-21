import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserRegistrationComponent } from './components/user-registration/user-registration.component';
import { UserLoginComponent } from './components/user-login/user-login.component';
import { PropertyListingComponent } from './components/property-listing/property-listing.component';
import { PropertyDetailsComponent } from './components/property-details/property-details.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { MessagingSystemComponent } from './components/messaging-system/messaging-system.component';

// Combine all routes here
const routes: Routes = [
  { path: 'register', component: UserRegistrationComponent },
  { path: 'login', component: UserLoginComponent },
  { path: 'properties', component: PropertyListingComponent },
  { path: 'property/:id', component: PropertyDetailsComponent },
  { path: 'profile', component: UserProfileComponent },
  { path: 'messages', component: MessagingSystemComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' }, 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}

// Optional export of routes if needed elsewhere
export { routes };