import { Injectable } from '@angular/core';
import { Recipe } from './recipe'
import { RECIPES } from './mock-recipes'
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RecipeService {

  private recipesUrl = 'http://127.0.0.1:8000/test';

  constructor(private http: HttpClient) { }

  getRecipes(): Observable<Recipe[]> {
    return this.http.get<Recipe[]>(this.recipesUrl);
  }
}
