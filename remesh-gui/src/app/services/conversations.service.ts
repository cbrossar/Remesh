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

  newConversation(title: string) {
    return this.http.post(environment.apiEndpointServer + '/conversations', {'title': title});
  }

  searchConversations(search_term: string) {
    return this.http.post(environment.apiEndpointServer + '/conversations/search', {'search_term': search_term});
  }
}
