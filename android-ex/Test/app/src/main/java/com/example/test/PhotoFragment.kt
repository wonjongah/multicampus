package com.example.test

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import kotlinx.android.synthetic.main.fragment_photo.*

private const val ARG_URI = "uri"


class PhotoFragment : Fragment() {
    private var uri:String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        arguments?.let {
            uri = it.getString(ARG_URI)
        }
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_photo, container, false)
    }

    companion object {
        @JvmStatic
        fun newInstance(uri:String) =
            PhotoFragment().apply {
                arguments = Bundle().apply {
                    arguments = Bundle().apply{
                        putString(ARG_URI, uri)
                    }
                }
            }
    }
}