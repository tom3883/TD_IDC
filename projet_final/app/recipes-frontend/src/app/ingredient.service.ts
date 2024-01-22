import { Injectable } from '@angular/core';
import { Recipe } from './recipe'
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { log } from 'console';

@Injectable({
  providedIn: 'root'
})

export class IngredientService {

  private recipesUrl = 'http://localhost:8000/getRecipes/cake';

  constructor(private http: HttpClient) { }

  getRecipes(): Observable<Recipe[]> {
    return this.http.get<Recipe[]>(this.recipesUrl);
  }

  searchRecipes(query: string) {
    const encodedQuery = query.replace(/ /g, '+'); 
    console.log(encodedQuery); 
    this.recipesUrl = 'http://localhost:8000/getRecipes/'+encodedQuery;
  }
}
