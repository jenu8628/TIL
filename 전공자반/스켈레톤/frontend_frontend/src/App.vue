<template>
  <div id="app">
    <div>
      <b-nav tabs align="right" v-if="this.$store.getters['getAccToken']">
        <b-nav-item disabled
          >{{ this.$store.getters.getUserId }} 님 반갑습니다</b-nav-item
        >
        <b-nav-item @click="onClickLogout">
          로그아웃
        </b-nav-item>
        <b-nav-item to="/me"> 내 정보 </b-nav-item>
      </b-nav>
      <b-nav tabs align="right" v-else>
        <b-nav-item to="/login"> 로그인 </b-nav-item>
        <b-nav-item to="/signup"> 회원가입 </b-nav-item>
      </b-nav>
    </div>

    <div>
      <router-link to="/">
        <img id="Logo" alt="Logo" src="./assets/newlogo.png" />
      </router-link>
    </div>

    <div>
      <b-nav id="nav" tabs align="left">
        <b-nav-item to="/">
          홈
        </b-nav-item>
        <b-nav-item to="/board">
          커뮤니티
        </b-nav-item>
        <b-nav-item to="/notice">
          공지사항
        </b-nav-item>
        <!-- <b-nav-item>
          Page4
        </b-nav-item> -->
      </b-nav>
    </div>
    <router-view />

    <div>
      <div class="container-fluid">
        <div class="jumbotron text-center mt-3">
          <p>(주) SSAFY.com | 대표 이호석 | 사업자등록번호 000-00-00000</p>
          <p>
            대전광역시 유성구 덕명동 124 | 이메일주소 : ssafy@ssafy.com | 호스팅
            제공자 : (주) SSAFY.com | 정보관리책임자 : 박성호
          </p>
          <p style="font-size:20px">SSAFY.com © All Rights Reserved.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
export default {
  created() {
    let token = JSON.parse(localStorage.getItem("vuex"))["token"]["acc_token"];
    axios.defaults.headers.common["Authorization"] = token;
  },
  methods: {
    onClickLogout() {
      alert("로그아웃이 완료되었습니다.");
      localStorage.removeItem("vuex");
      this.$store.dispatch("logout_token");
      this.$store
        .dispatch("logout_user")
        .then(() => this.$router.replace("/").catch(() => {}));
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
