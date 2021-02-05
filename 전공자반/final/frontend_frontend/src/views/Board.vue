<template>
  <div class="container mt-5 mb-5">
    <h1 align="center" style="margin-bottom: 50px">커뮤니티</h1>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  created() {
    this.$store.dispatch("delete_searchdata");
  }
};
</script>

<style></style>
