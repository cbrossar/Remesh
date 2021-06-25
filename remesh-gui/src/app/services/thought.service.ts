import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ThoughtService {

  constructor(private http: HttpClient) { }

  newThought(message_id: number, text: string) {
    return this.http.post(environment.apiEndpointServer + '/thoughts', {'message': message_id, 'text': text});
  }
}
