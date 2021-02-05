<template>
  <div>
    <b-container fluid class="mt-5 mb-5" style="width:600px">
      <b-row class="my-1 mb-5" style="width:500px">
        <b-col sm="3">
          <label>아이디</label>
        </b-col>
        <b-col sm="9">
          <b-form-input
            v-model="user.user_id"
            type="text"
            disabled
          ></b-form-input>
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
      <b-row class="my-1 mb-5" style="width:500px">
        <b-col sm="3">
          <label>이메일</label>
        </b-col>
        <b-col sm="9">
          <b-form-input
            v-model="user.user_email"
            @keypress.enter="login"
            type="email"
          ></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1 mb-5">
        <b-col sm="12">
          <b-button @click="changeInfo" variant="primary">수정하기</b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "@/plugins/axios";

export default {
  name: "Me",
  created() {
    var check = null;
    axios
      .get("/api/user/info")
      .then(response => {
        check = response.response.data["token"];
        if (check == "token") {
          check = null;
          let token = JSON.parse(localStorage.getItem("vuex"))["token"][
            "ref_token"
          ];
          console.log("ref 토큰 보내기" + token);
          axios.defaults.headers.common["Authorization"] = token;
          axios.get("/api/user/info").then(res => {
            console.log("재시도");
            if (res.status == 200) {
              let token = JSON.parse(localStorage.getItem("vuex"))["token"][
                "acc_token"
              ];
              axios.defaults.headers.common["Authorization"] = token;
              console.log("토큰재발급" + res.data["token"]);
              this.$store.dispatch("update_token", [res.data["token"], token]);
              this.user.user_id = this.$store.getters.getUserId;
              this.user.user_email = this.$store.getters.getUserEmail;
            }
          });
        } else if (check == "fail") {
          this.$store.dispatch("logout_token");
          alert("로그인 해주세요.");
          this.$rotuer.push("/login");
        }
      })
      .catch(() => {
        this.user.user_id = this.$store.getters.getUserId;
        this.user.user_email = this.$store.getters.getUserEmail;
      });
  },
  data() {
    return {
      user: {
        user_id: "",
        user_password: "",
        user_email: ""
      }
    };
  },
  methods: {
    changeInfo() {
      axios.put("api/user/modify", this.user).then(response => {
        if (response.status != 200) {
          alert("정보변경실패");
          return;
        }
        alert("성공정으로 변경되었습니다. 다시 로그인해주세요");
        this.$store.dispatch("logout_token");
        this.$store
          .dispatch("logout_user")
          .then(() => this.$router.replace("/").catch(() => {}));
      });
    }
  }
};
</script>

<style></style>
