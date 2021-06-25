import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ConversationsService {

  constructor(private http: HttpClient) {}

  
  getConversations() {
    return this.http.get(environment.apiEndpointServer + '/conversations');
  }
}
