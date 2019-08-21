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
import Sidebar from "../components/layout/Sidebar.vue";
import axios from "axios";

const APIHost = process.env.VUE_APP_API_HOST;

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
        .post(`${APIHost}/favorite_things/`, newItem)
    },
    updateFavoriteThing(newItem) {
      axios
        .put(`${APIHost}/favorite_things/${newItem.id}/`, newItem)
    },
    addNewCategory(newItem) {
      axios
        .post(`${APIHost}/category/`, newItem)
        .then(res => (this.categories = [...this.categories, res.data]))
    },
    switchCategory(url) {
      axios
        .get(url)
        .then(res => (this.favoriteThingsObj = res.data))
    }
  },
  created() {
    axios
      .get(`${APIHost}/category/`)
      .then(res => {
        this.categories = res.data.results;
        if (this.categories.length > 0) {
          axios
            .get(this.categories[0].url)
            .then(res => (this.favoriteThingsObj = res.data))
        }
      })
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
