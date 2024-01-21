import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductsComponent } from './products/products.component';
import { RecipesComponent } from './recipes/recipes.component';
const routes: Routes = [
  { path: '', component: RecipesComponent },
  { path: 'searchProducts', component: ProductsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
