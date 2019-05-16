import Component from '@ember/component';
import config from './../config/environment'

export default Component.extend({
    actions: {
        login(){
            $.post(`${window.location.protocol}//${window.location.hostname}:${config.backendport}`+'/login', {"username": this.username}, (data)=>{
                this.set('msg', `${data.name} ${data.msg} ${data.count}`)
            })
        }
    }
});
