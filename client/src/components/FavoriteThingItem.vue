<template>
  <div role="tablist">
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button
          block
          href="#"
          v-b-toggle="'accordion-' + favoriteThing.id"
          variant="secondary"
        >{{favoriteThing.title}}</b-button>
      </b-card-header>
      <b-collapse
        v-bind:id="'accordion-'+favoriteThing.id"
        accordion="my-accordion"
        role="tabpanel"
      >
        <b-card-body>
          <b-card-text>Rank: {{favoriteThing.ranking}}</b-card-text>
          <b-card-text>{{ favoriteThing.description }}</b-card-text>
          <b-button v-b-modal="'edit-modal-'+favoriteThing.id" variant="outline-secondary" block>Edit</b-button>
          <AddNewFavoriteThing
            modalTitle="Edit Favorite Item"
            v-bind:modalId="'edit-modal-'+favoriteThing.id"
            v-bind:itemId="favoriteThing.id"
            v-bind:initialTitle="favoriteThing.title"
            v-bind:initialRank="favoriteThing.ranking"
            v-bind:initialDescription="favoriteThing.description"
            v-bind:initialCategory="favoriteThing.category_id"
            v-bind:initialMetadata="favoriteThing.metadata"
            v-bind:categories="categories"
            v-on:addNewFavoriteThing="(newItem)=>$emit('addNewFavoriteThing',newItem)"
            v-on:updateFavoriteThing="(newItem)=>$emit('updateFavoriteThing',newItem)"
          />
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>

<script>
import AddNewFavoriteThing from "./AddNewFavoriteThing.vue";

export default {
  name: "FavoriteThingItem",
  props: ["favoriteThing", "categories"],
  components:{
      AddNewFavoriteThing
  }
};
</script>
