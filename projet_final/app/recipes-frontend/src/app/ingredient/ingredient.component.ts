import { Component, OnInit } from '@angular/core';
import { IngredientService } from '../ingredient.service';
import { Recipe } from '../recipe';

@Component({
  selector: 'app-products',
  templateUrl: './ingredient.component.html',
  styleUrls: ['./ingredient.component.css']
})
export class IngredientComponent implements OnInit {

  recipes: Recipe[] = [] ;

  constructor(private ingredientService: IngredientService) { }

  ngOnInit(): void {
  }

  getRecipes(): void {
    this.ingredientService.getRecipes().subscribe(recipes => this.recipes = recipes);
  }

  onSearchChanged(query: string) {
    this.ingredientService.searchRecipes(query);
    this.getRecipes();
  }

}
