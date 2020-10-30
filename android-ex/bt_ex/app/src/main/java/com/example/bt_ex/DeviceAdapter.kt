package com.example.bt_ex

import android.bluetooth.BluetoothDevice
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.item_bluetoothdevice.view.*

class DeviceAdapter(val deviceList: List<BluetoothDevice>, val onItemClick: (device: BluetoothDevice)->Unit ):
    RecyclerView.Adapter<DeviceAdapter.ViewHolder>() {
        class ViewHolder(val layoutView: View) : RecyclerView.ViewHolder(layoutView)
    {
        val txtName = layoutView.txtName
        val txtAddress = layoutView.txtAddress
        fun bind(device: BluetoothDevice) {
            txtName.text = device.name
            txtAddress.text = device.address.toString()
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val layout = LayoutInflater.from(parent.context).inflate(R.layout.item_bluetoothdevice, parent, false)
        return ViewHolder(layout) // layout -> LinearLayout
    }

    override fun getItemCount(): Int = deviceList.size

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val device = deviceList[position]
        holder.bind(device) // 내용묶기
        holder.layoutView.setOnClickListener {
            onItemClick(device)
            // holder.layoutView => LinearLayout 얘한테 클릭리스너
        }
    }
}