import { Component, OnInit } from '@angular/core';
import { Recipe } from '../recipe';
import { Product } from '../product';
import { RecipeService } from '../recipe.service';

@Component({
  selector: 'app-recipes',
  templateUrl: './recipes.component.html',
  styleUrls: ['./recipes.component.css']
})
export class RecipesComponent implements OnInit {

  recipes: Recipe[] = [] ;

  constructor(private recipeService: RecipeService) { }

  ngOnInit(): void {
  }

  getRecipes(): void {
    this.recipeService.getRecipes().subscribe(recipes => this.recipes = recipes);
  }

  onSearchChanged(query: string) {
    this.recipeService.searchRecipes(query);
    this.getRecipes();
  }
}
