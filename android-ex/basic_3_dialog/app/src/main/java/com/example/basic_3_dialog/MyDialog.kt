package com.example.basic_3_dialog

import android.app.Dialog
import android.content.Context
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.dialog_my.*


class MyDialog(ctx: Context) : Dialog(ctx) {

    open var dayString = ""
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.dialog_my)

        // 캘린더 control의 일정 바뀔 경우
        // 발생하는 이벤트 핸들러 등록 및 구현
        calendarView.setOnDateChangeListener{view, year, month, dayOfMonth ->
            dayString = "${year}-${month+1}-${dayOfMonth}"
            dismiss() // 다이얼로그 닫기
        }

    }
}