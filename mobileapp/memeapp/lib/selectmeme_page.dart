import 'package:flutter/material.dart';
import 'package:memeapp/editmeme_page.dart';
import 'meme_data.dart';

class SelecMeme extends StatefulWidget {
  const SelecMeme({Key? key}) : super(key: key);

  @override
  _SelecMemeState createState() => _SelecMemeState();
}

class _SelecMemeState extends State<SelecMeme> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          elevation: 0,
          backgroundColor: Colors.white,
          title: Text(
            'select meme',
            style: TextStyle(color: Colors.black),
          ),
        ),
        body: SafeArea(
          child: ListView(
            children: [
              Wrap(
                spacing: 2,
                runSpacing: 2,
                children: [
                  for (var i = 0; i < 40; i++)
                    RawMaterialButton(
                      onPressed: () {
                        print(memeName[i]);
                        Navigator.push(context, MaterialPageRoute(
                          builder: (context) {
                            return EditMeme(imageName: memeName[i]);
                          },
                        ));
                      },
                      child: Container(
                        width: (MediaQuery.of(context).size.width - 4) / 3,
                        height: (MediaQuery.of(context).size.width - 4) / 3,
                        child: Image.asset(
                          'assets/meme/${memeName[i]}.jpg',
                          fit: BoxFit.cover,
                        ),
                      ),
                    )
                ],
              )
            ],
          ),
        ));
  }
}
