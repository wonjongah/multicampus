package com.example.bt_ex

import android.bluetooth.BluetoothDevice
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_bluetooth.*
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.toast
import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.io.PrintWriter
import java.lang.Exception
import java.util.*

class BluetoothActivity : AppCompatActivity() {

    var out : PrintWriter? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_bluetooth)

        btnSend.setOnClickListener {
            // 메시지 전송
            out?.print("${editMessage.text}\r\n") // 메모리에만..
            out?.flush() // 진짜
            editMessage.setText("")
        }

        val device = intent.getParcelableExtra<BluetoothDevice>("device")!!
        // 일반객체는 getParcelableExtra로 꺼낸다
        // !! -> null 아님을 보장한다
        BtWorkThread(device).start() // 스레드 기동
    }

    inner class BtWorkThread(val device: BluetoothDevice):Thread(){
        override  fun run(){
            try{
                var uuid = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
                // 시리얼 통신을 할 것이다
                val socket = device.createRfcommSocketToServiceRecord(uuid);
                socket.connect(); // 반드시 작업스레드에서 해야 하는 작업
                // 동기함수 접속 될 때까지 기다림, 접속 안 되면 예외
                runOnUiThread{toast("블루투스 연결 성공")}
                
                val br = BufferedReader(InputStreamReader(socket.getInputStream())) //rx
                // reader 텍스트 기반
                // 바이너리 기반을 reader로 바꾸겠다
                out = PrintWriter(OutputStreamWriter(socket.getOutputStream()))//tx
                // writer 텍스트 기반 출력
                // 바이너리 기반을 writer로 바꾸겠다

                while(!Thread.currentThread().isInterrupted()){
                    val message = br.readLine(); // 개행문자 나올 때까지 내부적으로 읽어서 리턴, 리턴엔 개행문자 빠짐
                    // br.readLine() 작업스레드에서!!
                    runOnUiThread{
                        receiveMsgView.text = "$message\n${receiveMsgView.text}";
                    }
                }
                socket.close()
            }
            catch (e:Exception){
                runOnUiThread{toast("블루투스 연결 실패")}
                finish();
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy();

//        btThread?.interrupt()
    }
}