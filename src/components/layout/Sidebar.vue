<template>
  <div>
    <p class="subtitle">Add New</p>
    <div>
      <b-button v-b-modal.new-category-modal block variant="outline-secondary">Category</b-button>
      <AddNewCategory v-on:addNewCategory="(newItem)=>$emit('addNewCategory',newItem)"/>
    </div>
    <div class="container_y">
      <b-button v-b-modal.new-favorite-thing-modal block variant="outline-secondary">Favorite Item</b-button>
      <AddNewFavoriteThing
        v-bind:categories="categories"
        modalTitle="Add New Favorite Item"
        modalId="new-favorite-thing-modal"
        title="test"
        v-on:addNewFavoriteThing="(newItem)=>$emit('addNewFavoriteThing',newItem)"
      />
    </div>
  </div>
</template>
 
<script>
import AddNewCategory from "../AddNewCategory.vue";
import AddNewFavoriteThing from "../AddNewFavoriteThing.vue";

export default {
  name: "Sidebar",
  props: ["categories"],
  components: {
    AddNewCategory,
    AddNewFavoriteThing
  }
};
</script>
<style>
.container_y {
  margin-top: 5px;
}
</style>
