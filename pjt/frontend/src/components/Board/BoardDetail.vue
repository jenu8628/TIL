<template>
  <div>
    <table class="table table-hover" style="margin-top:70px">
      <thead>
        <tr>
          <th colspan="4">
            <h4 style="margin-top:10px; margin-bottom:10px">
              {{ detail.board_title }}
            </h4>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td width="70%"></td>
          <td style="text-align:right" width="10%">
            <b>{{ detail.board_writer }}</b>
          </td>
          <td style="text-align:right" width="10%">
            조회수 {{ detail.board_cnt }}
          </td>
          <td style="text-align:right" width="10%">{{ detail.write_date }}</td>
        </tr>
      </tbody>
    </table>
    <div>
      <h5 style="margin-top:60px; margin-bottom:200px">
        {{ detail.board_content }}
      </h5>
    </div>
    <comment></comment>
    <div
      v-if="
        this.$store.getters.getUserInfo == 1 ||
          this.$store.getters.getUserId == detail.board_writer
      "
    >
      <button @click="delBoard" class="btn btn-primary mb-5 mr-2">
        귿삭제
      </button>
      <button @click="modifyBoard" class="btn btn-primary mb-5 ml-2">
        글수정
      </button>
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import Comment from "./Comment.vue";
export default {
  components: { Comment },
  created() {
    axios.get("/api/board/" + this.$route.params.bno).then(response => {
      this.detail = response.data;
    });
  },
  data() {
    return {
      detail: {}
    };
  },
  methods: {
    delBoard() {
      axios.delete("/api/board/" + this.$route.params.bno).then(response => {
        if (response.status == 200) {
          alert("게시글 삭제 완료");
          this.$router.push("/board");
        } else {
          alert("게시글 삭제 실패");
        }
      });
    },
    modifyBoard() {
      this.$router.push("/board/" + this.$route.params.bno + "/modify");
    }
  }
};
</script>

<style></style>
