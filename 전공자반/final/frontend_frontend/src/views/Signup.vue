<template>
  <div>
    <b-container fluid class="mt-5 mb-5" style="width:600px">
      <b-row class="my-1 mb-5" style="width:600px">
        <b-col sm="2">
          <label>아이디</label>
        </b-col>
        <b-col sm="7">
          <b-form-input v-model="user.user_id" type="text"></b-form-input>
        </b-col>
        <b-col sm="3">
          <b-button @click="checkid" variant="secondary">중복확인</b-button>
        </b-col>
      </b-row>
      <b-row class="my-1 mb-5" style="width:600px">
        <b-col sm="2">
          <label>패스워드</label>
        </b-col>
        <b-col sm="7">
          <b-form-input
            v-model="user.user_password"
            @keypress.enter="login"
            type="password"
          ></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1 mb-5" style="width:600px">
        <b-col sm="2">
          <label>이메일</label>
        </b-col>
        <b-col sm="7">
          <b-form-input
            v-model="user.user_email"
            @keypress.enter="login"
            type="email"
          ></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1 mb-5">
        <b-col sm="11">
          <b-button @click="signup" variant="primary">회원가입</b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "@/plugins/axios";

export default {
  name: "Signup",
  data() {
    return {
      user: {
        user_id: "",
        user_password: "",
        user_email: ""
      },
      idCheck: 0,
      message: ""
    };
  },
  methods: {
    signup() {
      if (
        this.user.user_id.length <= 0 ||
        this.user.user_password.length <= 0 ||
        this.user.user_email.length <= 0
      ) {
        alert("정보를 모두 입력해주세요.");
        return;
      }
      if (this.idCheck == 0) {
        alert("아이디 중복을 확인하세요.");
        return;
      }
      axios.post("api/login/signup", this.user).then(response => {
        if (response.status != 200) {
          alert("회원가입 실패");
          return;
        }
        alert("회원가입 성공!");
        this.$router.replace("/");
      });
    },
    checkid() {
      axios
        .post("api/login/signup/check", { user_id: this.user.user_id })
        .then(response => {
          if (response.status != 200) {
            alert("중복된 아이디입니다.");
            return;
          }
          alert("사용가능한 아이디입니다.");
          this.idCheck = 1;
        });
    }
  }
};
</script>

<style></style>
