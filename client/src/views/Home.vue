<template>
  <div id="app">
    <b-container class="bv-example-row">
      <b-row class="text-center">
        <b-col md="3">
          <Categories v-bind:categories="categories" v-on:switchCategory="switchCategory"/>
        </b-col>
        <b-col md="7">
          <FavoriteThings
            v-bind:favoriteThingsObj="favoriteThingsObj"
            v-bind:categories="categories"
            v-on:updateFavoriteThing="updateFavoriteThing"
          />
        </b-col>
        <b-col md="2">
          <Sidebar
            v-bind:categories="categories"
            v-on:addNewFavoriteThing="addNewFavoriteThing"
            v-on:addNewCategory="addNewCategory"
          />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import FavoriteThings from "../components/FavoriteThings.vue";
import Categories from "../components/Categories.vue";
import Category from "../components/Category.vue";
import Sidebar from "../components/layout/Sidebar.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    FavoriteThings,
    Categories,
    Sidebar
  },
  data() {
    return {
      favoriteThingsObj: {},
      categories: []
    };
  },
  methods: {
    addNewFavoriteThing(newItem) {
      axios
        .post("http://127.0.0.1:8000/favorite_things/", newItem)
        .then(res => console.log(res.data))
        .catch(err => console.log(err));
    },
    updateFavoriteThing(newItem){
      axios
        .put(`http://127.0.0.1:8000/favorite_things/${newItem.id}/`, newItem)
        .then(res => console.log(res.data))
        .catch(err => console.log(err));
    },
    addNewCategory(newItem) {
      axios
        .post("http://127.0.0.1:8000/category/", newItem)
        .then(res => (this.categories = [...this.categories, res.data]))
        .catch(err => console.log(err));
    },
    switchCategory(url) {
      axios
        .get(url)
        .then(res => (this.favoriteThingsObj = res.data))
        .catch(err => console.log(err));
    }
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/category/")
      .then(res => {
        this.categories = res.data.results;
        axios
          .get(this.categories[0].url)
          .then(res => (this.favoriteThingsObj = res.data))
          .catch(err => console.log(err));
      })
      .catch(err => console.log(err));
  }
};
</script>
<style>
#app {
}
.subtitle {
  color: gray;
  margin-top: 10px;
  margin-bottom: 0px;
}
</style>
