def test_gene():
    # print("hoge")
    yield "a"
    yield "b"
    yield "c"


# 文字列でアルファベットすべてを一文字ずつ生成するジェネレータを定義する。
def gene_alphabet():
    for i in range(26):
        yield chr(ord("a") + i)


# どっかのなかでStopIterationをraiseさせる。
def gene_error():
    for i in range(26):
        if i == 12:
            raise StopIteration
            # raise Exception("エラーだ!!!")
        yield chr(ord("a") + i)


# どうにかして回り切ったイテレータに対してNextしたい。
def wrong_iter():
    for i in range(1, 10):
        yield i


if __name__ == '__main__':
    for itm in test_gene():
        print(itm)

    print("\n\n\n上はtest_geneジェネレータのテストです。")
    for itm in gene_alphabet():
        print(itm)
    print("\n\n\n上はgene_alphabetジェネレータのテストです。")

    # try-catch構文でエラーをキャッチする
    print("\n\n\ntry-catch構文でジェネレタの中のエラーをキャッチする")
    try:
        for itm in gene_error():
            print(itm)
    except Exception as e:
        print("エラーが発生しました。")
        print(e)

    print("イテレータを定義するけど、範囲外でnextしてみる。")
    # rangeで1-10までのイテレータを定義して、1-10までのループする。
    itr = iter(range(1, 11))
    # for i in range(11):
    #    print(next(itr))
    # ↑のforブロックをコメントアウトするとここでエラー死するのでコメントにしとく

    print("\n\n\nループのまえでnext()しておくとその次のやつからループするのか。")
    itr = iter(range(1, 11))
    tmp = next(itr)
    # itrをforする。2から表示される?
    for i in range(1, 12):
        print(tmp)

    print("\n\n\nジェネレータ関数のなかでgenerator raised StopIterationを出したい。")
    for itm in wrong_iter():
        print(itm)
    # ↑検証の用は済んだのでほっとく。
