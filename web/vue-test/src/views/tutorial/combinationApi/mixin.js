const myMixin = {
    data(){
        return{
            sayFor:"world(mixin)"
        }
    },
    created(){
        console.log(`mixin say hi ${this.sayFor} mixin is created`)
    },
    methods: {
        sayHello(){
            console.log(`mixin say hello ${this.sayFor}`)
        }
    },
}

export default myMixin