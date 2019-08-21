<template>
  <div>
    <header class="header">
      <router-link to="/">Favorite Things</router-link>
    </header>
  </div>
</template>

<script>
export default {
  name: "Header"
};
</script>


<style scoped>
.header {
  background: #343a40;
  color: gray;
  text-align: center;
  padding: 15px;
}
.header a {
  color: rgba(255, 255, 255, 0.5);
  text-decoration: none;
}
</style>
