package com.example.bt_ex

import android.app.Activity
import android.bluetooth.BluetoothAdapter
import android.bluetooth.BluetoothDevice
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.startActivity
import org.jetbrains.anko.toast

class MainActivity : AppCompatActivity() {

    val bluetoothAdapter: BluetoothAdapter? by lazy{ // 널이 아니면
        // by lazy로 초기화를 늦추는 것
        BluetoothAdapter.getDefaultAdapter() // 얘가 사용 가능해졌을 때 블럭 안 리턴값으로 초기화하겠다
    } // null이면 블루투스 장치 없다
    private val REQUEST_ENABLE_BT = 100

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if(bluetoothAdapter == null){
            toast("단말기는 블루투스를 지원하지 않습니다")
            finish()
            return
        }
        checkBluetoothDevices()

        btnCheck.setOnClickListener {
            scanDevice()
        }
    }
    
    fun checkBluetoothDevices(){
        if(bluetoothAdapter!!.isEnabled){ // !! -> 이 변수는 널이 아니므로 안심해도 된다
            // 원래 내부적으로 if 돌아서 null인지 확인함
            // !! -> if 들어가지 않고 바로 접근
            stateBluetooth.text = "Bluetooth is Enable"
            btnCheck.isEnabled = true
            scanDevice()
        }else{
            stateBluetooth.text = "Bluetooth is Not Enabled"
            var enableBtIntent = Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE)
            startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT)

            // forResult, 새로운 액티비티가 뜰 것이고 사용자의 결과를 받겠다
            // 응답을 받겠다
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if(requestCode == REQUEST_ENABLE_BT){
            if(resultCode == Activity.RESULT_OK){
                stateBluetooth.text = "Bluetooth is Enabled"
                toast("블루투스가 활성화되었습니다")
            }else{
                stateBluetooth.text = "Bluetooth is not Enabled"
                toast("블루투스 활성화 요청이 취소되었거나 예외 발생")
            }
        }
        super.onActivityResult(requestCode, resultCode, data)
    }

    fun scanDevice(){
        // 페어링되어있는 디바이스 집합 추출
        val devices = bluetoothAdapter!!.bondedDevices // MutableMap (장치명key, 디바이스value)
        if(devices.size == 0){
            stateBluetooth.text = "연결된 블루투스가 없습니다"
        }else{
            stateBluetooth.text = "페어링 블루투스 장비 (${devices.size}개"
            val adapter = DeviceAdapter(devices.toList(), ::onItemClick)
            listDevice.adapter = adapter
            // toList -> value 파트를 리스트로 만들어줌
        }
    }

    fun onItemClick(device:BluetoothDevice){
        startActivity<BluetoothActivity>("device" to device)
        // device -> intent에 저장된다
        toast("${device.name} 선택")
    }
}