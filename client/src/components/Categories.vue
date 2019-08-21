<template>
  <div>
    <p class="subtitle">Categories</p>
    <div v-bind:key="category.id" v-for="category in categories">
      <b-list-group>
        <Category
          v-on:switchCategory="(url)=>$emit('switchCategory',url)"
          v-bind:category="category"
        />
      </b-list-group>
    </div>
  </div>
</template>

<script>
import Category from "./Category.vue";

export default {
  name: "Categories",
  props: ["categories"],
  components: {
    Category
  }
};
</script>


<style scoped>
</style>
