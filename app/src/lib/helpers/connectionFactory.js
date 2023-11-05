import axios from 'axios'

export default class ConnectionFactory{

    static async postRequest(link, data){
        let response = await axios.post(link, data)
        return response.data
    }

    static async getRequest(link){
        let response = await axios.get(link)
        return response.data
    }

}