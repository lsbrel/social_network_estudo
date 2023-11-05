import swal from 'sweetalert'

export default class AlertShower{

    static errorAlert(message){
        return swal({
            icon: 'error',
            text: message,
            buttons: false,
            timer: 1000
        })
    }

    static successAlert(message){
        return swal({
            icon: 'success',
            text: message,
            buttons: false,
            timer: 1000
        })
    }

}