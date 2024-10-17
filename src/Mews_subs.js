public class Main {
    public class Main {
        import { pushStatus } from "pwa/pushStatus"
    import { urlB64ToUint8Array } from "utils"
    
    const pushSubscribe = () => {
        const publicKey = urlB64ToUint8Array(vapid.data.publicKey)
        const option = {
            userVisibleOnly: true,
            applicationServerKey: publicKey,
        }
    
        navigator.serviceWorker.ready.then(registration => {
            registration.pushManager
                .subscribe(option)
                .then(subscription => {
                    // 구독 요청 성공 시 받는 PushSubscription객체
                    postSubscribe(subscription) // 서버에게 전달
                    // 클라이언트에서 푸시 관련 상태를 별도의 객체(pushStatus)를 만들어 관리했다.
                    pushStatus.pushSubscription = subscription
                })
                .catch(() => {
                    pushStatus.pushSubscription = null
                })
        })
    }
        
    }
    
    
}
