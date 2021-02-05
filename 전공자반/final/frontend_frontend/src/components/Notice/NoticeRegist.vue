<template>
  <div>
    <b-form-input
      id="title"
      size="lg"
      style="margin-bottom:50px"
      v-model="notice_title"
    ></b-form-input>
    <b-form-textarea
      id="textarea"
      style="margin-bottom:50px"
      v-model="notice_content"
      rows="15"
      size="lg"
      max-rows="15"
    ></b-form-textarea>
    <button @click="regist" class="btn btn-primary mb-5">
      글쓰기
    </button>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
export default {
  data() {
    return {
      notice_title: "",
      notice_content: ""
    };
  },
  methods: {
    regist() {
      axios
        .post("/api/notice", {
          notice_title: this.notice_title,
          notice_content: this.notice_content
        })
        .then(response => {
          if (response.status == 200) {
            alert("정상적으로 등록되었습니다.");
            this.$router.push("/notice");
          } else {
            alert("등록에 실패하였습니다.");
          }
        });
    }
  }
};
</script>

<style></style>
