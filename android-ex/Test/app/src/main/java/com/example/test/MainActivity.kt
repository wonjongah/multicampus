package com.example.test


import android.Manifest
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.longToast
import kotlin.concurrent.timer

class MainActivity : AppCompatActivity() {
    lateinit var permissionChecker: PermissionChecker

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val permissions = arrayOf(
            Manifest.permission.READ_EXTERNAL_STORAGE)
        permissionChecker = PermissionChecker(this, permissions)
        if (permissionChecker.check()) {
// 초기화
            init()
//            longToast("권한 획득 했었음")
        }
    }
    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray) {
        super.onRequestPermissionsResult(
            requestCode, permissions,grantResults)
        if(permissionChecker.checkGranted(
                requestCode, permissions,grantResults)){
// 모든 권한 획득 성공
// 초기화
            init()
//            longToast("권한 획득 성공")
        } else {
// 권한 획득 실패
            longToast("권한 거부 됨")
        }
    }
    private fun init() {
        val mediaImage = MediaImage(this)
        val adapter = PhotoPagerAdapter(supportFragmentManager, mediaImage.getAllPhotos()
        )
        viewPager.adapter = adapter
// 3초마다 자동으로 슬라이드
        timer(period = 3000) {
            runOnUiThread {
                if (viewPager.currentItem < adapter.count - 1) {
                    viewPager.currentItem = viewPager.currentItem + 1
                } else {
                    viewPager.currentItem = 0
                }
            }
        }
    }
}