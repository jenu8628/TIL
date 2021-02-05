<template>
  <div>
    <b-form-input
      id="title"
      size="lg"
      style="margin-bottom:50px"
      v-model="board_title"
    ></b-form-input>
    <b-form-textarea
      id="textarea"
      style="margin-bottom:50px"
      v-model="board_content"
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
      board_title: "",
      board_content: ""
    };
  },
  methods: {
    regist() {
      axios
        .post("/api/board", {
          board_title: this.board_title,
          board_content: this.board_content
        })
        .then(response => {
          if (response.status == 200) {
            alert("정상적으로 등록되었습니다.");
            this.$router.push("/board");
          } else {
            alert("등록에 실패하였습니다.");
          }
        });
    }
  }
};
</script>

<style></style>
