package com.example.recycleviewapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.activity_main.view.*

class MainActivity : AppCompatActivity() {

    var items: MutableList<MainData> = mutableListOf( // test 데이터
            // 3개의 mainData 인스턴스 구성
            MainData("Title1", "Content1"),
            MainData("Title2", "Content2"),
            MainData("Title3", "Content3"))

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        rv_main_list.adapter = MainAdapter(items)
        rv_main_list.layoutManager = GridLayoutManager(this, 3)

        // list와 adapter 연결
    }
}