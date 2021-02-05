<template>
  <div>
    <b-container fluid class="mt-5 mb-5" style="width:600px">
      <b-row class="my-1 mb-5" style="width:500px">
        <b-col sm="3">
          <label>아이디</label>
        </b-col>
        <b-col sm="9">
          <b-form-input v-model="user.user_id" type="text"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1 mb-5" style="width:500px">
        <b-col sm="3">
          <label>패스워드</label>
        </b-col>
        <b-col sm="9">
          <b-form-input
            v-model="user.user_password"
            @keypress.enter="login"
            type="password"
          ></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1 mb-5">
        <b-col sm="12">
          <b-button @click="login" variant="primary">로그인</b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Vue from "vue";
import VueRouter from "vue-router";
import axios from "@/plugins/axios";

Vue.use(VueRouter);

export default {
  data() {
    return {
      user: {
        user_id: "",
        user_password: ""
      },
      message: ""
    };
  },
  computed: {
    nextRoute() {
      return this.$route.params.nextRoute ? this.$route.params.nextRoute : "";
    }
  },
  methods: {
    login: function() {
      this.$store.dispatch("update_savepath", "");
      if (
        this.user.user_id.length <= 0 ||
        this.user.user_password.length <= 0
      ) {
        alert("아이디와 비밀번호를 모두 입력해주세요.");
        return false;
      }
      axios.post("/api/login", this.user).then(response => {
        if (response.status != 200) {
          alert("아이디나 패스워드가 틀렸습니다.");
          this.user.user_password = "";
          return false;
        }
        this.$store.dispatch("update_token", [
          response.data["acc_token"],
          response.data["ref_token"]
        ]);
        this.$store.dispatch("login_user", response.data["UserInfo"]);
        axios.defaults.headers.common["Authorization"] =
          response.data["acc_token"];
        this.$router.replace(`/${this.$store.getters.getSavePath}`);
      });
    }
  }
};
</script>
