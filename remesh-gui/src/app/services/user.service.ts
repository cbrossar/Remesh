import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  newUser(username: string) {
    return this.http.post(environment.apiEndpointServer + '/users', {'name': username});
  }

}
