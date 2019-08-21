<template>
  <div>
    <b-list-group-item href="#" @click="$emit('switchCategory', category.url)">{{category.name}}</b-list-group-item>
  </div>
</template>

<script>
export default {
  name: "Category",
  props: ["category"]
};
</script>


<style scoped>
</style>
