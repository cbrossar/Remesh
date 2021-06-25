import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ConversationsComponent } from './components/conversations/conversations.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { MessagesComponent } from './components/messages/messages.component';

const routes: Routes = [
  { path: "", component: LoginComponent },
  { path: "login", component: LoginComponent },
  { path: "home", component: HomeComponent },
  { path: "conversations", component: ConversationsComponent },
  { path: "conversations/:id/messages", component: MessagesComponent },

]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
