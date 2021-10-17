vue <template>
  <div class="contsiner mt-4">
    <form @submit.prevent="insertArticle">
  <input  type="text" class="form-control" v-model="title" style="width:50%"
  placeholder="Enter Your Title here"/>
  <br><br><br>
  <textarea rows="8" placeholder="Enter Article Body" 
 style="width:60%"
  class="form-control"  v-model="body">
  </textarea>
  <br><br>
  <button type="submit" class="btn btn-sucess mt-4">
    Publish Article 
    </button>
    </form>
  </div>
</template> 

<script>
import {csrftoken} from '../csrf/csrf_token';
export default {
data()
{
  return {
    title:null,
    body:null,
    error:null,
  }
},
methods:{
  insertArticle()
  {
    if(!this.title || !this.body)
    {
this.error ="Please fill the feilds"
    }
    else{
       fetch('api/articles/',{ 
                method:"POST",
                headers:{
                    'Contenet-Type':'application/json',
                'X-CSRFTOKEN':csrftoken 
        },
        body: JSON.stringify({title:this.title,body:this.body})
      })
      .then(resp=>resp.json())
      .then(()=> {
      this.$router.push({
        name:'Home'
      })
      
      })

    }
  }
}
}
</script>

<style>

</style>