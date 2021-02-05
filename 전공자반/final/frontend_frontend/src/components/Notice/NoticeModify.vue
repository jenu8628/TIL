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
    <button @click="modify" class="btn btn-primary mb-5">
      글수정
    </button>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
export default {
  created() {
    axios.get("/api/notice/" + this.$route.params.nno).then(response => {
      this.notice_title = response.data["notice_title"];
      this.notice_content = response.data["notice_content"];
    });
  },
  data() {
    return {
      notice_title: "",
      notice_content: ""
    };
  },
  methods: {
    modify() {
      axios
        .put("/api/notice/" + this.$route.params.nno, {
          notice_title: this.notice_title,
          notice_content: this.notice_content
        })
        .then(response => {
          if (response.status == 200) {
            alert("정상적으로 수정되었습니다.");
            this.$router.push("/notice/" + this.$route.params.nno);
          } else {
            alert("수정에 실패하였습니다.");
          }
        });
    }
  }
};
</script>

<style></style>
