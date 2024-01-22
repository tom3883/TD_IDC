import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { IngredientComponent } from './ingredient/ingredient.component';
import { RecipesComponent } from './recipes/recipes.component';
const routes: Routes = [
  { path: '', component: RecipesComponent },
  { path: 'searchIngredient', component: IngredientComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
