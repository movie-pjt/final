<template>
  <div class="comment-list d-flex flex-column">
    <div class="d-flex">
      <h3>댓글</h3>

    </div>
    <ul>
      <comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </comment-list-item>        
    </ul>

    <comment-list-form></comment-list-form>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentListForm from '@/components/CommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>
.comment-list {
  /* border: 1px solid blue; */
  width: 100%;
}
ul {
  list-style:none;
  padding-left: 0 !important;
}
</style>